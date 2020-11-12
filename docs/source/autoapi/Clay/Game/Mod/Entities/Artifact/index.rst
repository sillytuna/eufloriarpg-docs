
Artifact Class
==============



Namespace
    :dn:ns:`Clay.Game.Mod.Entities`

Assemblies
    * Clay.Game

----

.. contents::
   :local:



Inheritance Hierarchy
---------------------

* :dn:cls:`System.Object`
* :dn:cls:`Tuna.Mob`
* :dn:cls:`Clay.Game.Mod.Entities.Entity`
* :dn:cls:`Clay.Game.Mod.Entities.Vehicle`
* :dn:cls:`Clay.Game.Mod.Entities.Equipment`
* :dn:cls:`Clay.Game.Mod.Entities.Artifact`




Syntax
------

.. code-block:: csharp

    public class Artifact : Equipment, IComparable, IAudioSourceInfo, ITargettable, IPathFindingAgent





.. dn:class:: Clay.Game.Mod.Entities.Artifact
    :hidden:

.. dn:class:: Clay.Game.Mod.Entities.Artifact


Constructors
------------

.. dn:class:: Clay.Game.Mod.Entities.Artifact
    :noindex:
    :hidden:

    .. dn:constructor:: Clay.Game.Mod.Entities.Artifact.Artifact()




        .. code-block:: csharp

            public Artifact()



Properties
----------

.. dn:class:: Clay.Game.Mod.Entities.Artifact
    :noindex:
    :hidden:

    .. dn:property:: Clay.Game.Mod.Entities.Artifact._activatedAcceleration



        :rtype: System.Single

        .. code-block:: csharp

            public float _activatedAcceleration { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Artifact._activatedCollisionsDisabled



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool _activatedCollisionsDisabled { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Artifact._activatedDrag



        :rtype: System.Single

        .. code-block:: csharp

            public float _activatedDrag { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Artifact._activatedSpeed



        :rtype: System.Single

        .. code-block:: csharp

            public float _activatedSpeed { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Artifact._activatedWorldObject



        :rtype: System.String

        .. code-block:: csharp

            public string _activatedWorldObject { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Artifact._artifactType



        :rtype: System.String

        .. code-block:: csharp

            public string _artifactType { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Artifact._behaviourActivated



        :rtype: System.String

        .. code-block:: csharp

            public string _behaviourActivated { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Artifact._targetBehaviourActivated



        :rtype: System.String

        .. code-block:: csharp

            public string _targetBehaviourActivated { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Artifact.artifactDef



        :rtype: ArtifactDef

        .. code-block:: csharp

            public ArtifactDef artifactDef { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Artifact.artifactManagerIndex



        :rtype: System.Int32

        .. code-block:: csharp

            public int artifactManagerIndex { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Artifact.behaviourAffect



        :rtype: ArtifactDef.BehaviourAffects

        .. code-block:: csharp

            public ArtifactDef.BehaviourAffects behaviourAffect { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Artifact.isDamageable



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool isDamageable { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Artifact.isTargetable



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool isTargetable { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Artifact.isWeaponSwapping



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isWeaponSwapping { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Artifact.lifeCount



        :rtype: System.Single

        .. code-block:: csharp

            public float lifeCount { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Artifact.lifeCounter



        :rtype: System.Single

        .. code-block:: csharp

            public float lifeCounter { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Artifact.spawnHeader



        :rtype: System.String

        .. code-block:: csharp

            public override string spawnHeader { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Artifact.useSpawnEntityCommand



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool useSpawnEntityCommand { get; }



Methods
-------

.. dn:class:: Clay.Game.Mod.Entities.Artifact
    :noindex:
    :hidden:

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.Activate(Attributes, UnityEngine.Vector2, System.Single, Colony, Team)



        :type attr: Attributes

        :type atPosition: UnityEngine.Vector2

        :type atAngle: System.Single

        :type colony: Colony

        :type newTeam: Team


        .. code-block:: csharp

            public override void Activate(Attributes attr, Vector2 atPosition, float atAngle, Colony colony, Team newTeam)

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.Affects(System.Int32)



        :type typeID: System.Int32

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool Affects(int typeID)

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.CheckFollowingValidTarget()



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool CheckFollowingValidTarget()

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.CloneConfiguration(Tuna.Mob)



        :type mob: Tuna.Mob


        .. code-block:: csharp

            public override void CloneConfiguration(Mob mob)

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.Deactivate(System.Boolean)



        :type quietly: System.Boolean

        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool Deactivate(bool quietly)

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.Die(System.Boolean, System.Boolean, System.Boolean)



        :type exploded: System.Boolean

        :type trash: System.Boolean

        :type quietly: System.Boolean


        .. code-block:: csharp

            public override void Die(bool exploded = false, bool trash = true, bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.FindNewFollowTarget()




        .. code-block:: csharp

            public void FindNewFollowTarget()

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.GenerateCharacteristics()




        .. code-block:: csharp

            protected override void GenerateCharacteristics()

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.InitialiseApp()




        .. code-block:: csharp

            public static void InitialiseApp()

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.InitialiseLevel()




        .. code-block:: csharp

            public static void InitialiseLevel()

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.IsFollowTargetValidCB(Clay.Game.Mod.Entities.Entity, UnityEngine.Vector2)



        :type target: Clay.Game.Mod.Entities.Entity

        :type sourcePosition: UnityEngine.Vector2

        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool IsFollowTargetValidCB(Entity target, Vector2 sourcePosition)

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.LevelUp(System.Boolean)



        :type quietly: System.Boolean


        .. code-block:: csharp

            public void LevelUp(bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.OnEntityDiedOrTrashedListener(System.String, System.Object, System.Object, System.Object)



        :type ev: System.String

        :type sender: System.Object

        :type param1: System.Object

        :type param2: System.Object


        .. code-block:: csharp

            protected override void OnEntityDiedOrTrashedListener(string ev, object sender, object param1, object param2)

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.ParentColonised()




        .. code-block:: csharp

            public override void ParentColonised()

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.RecalculateExtents()




        .. code-block:: csharp

            protected override void RecalculateExtents()

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.Render()




        .. code-block:: csharp

            public override void Render()

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.SetIndex(System.Int32)



        :type index: System.Int32


        .. code-block:: csharp

            public void SetIndex(int index)

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.ShieldOwnerAttacked()




        .. code-block:: csharp

            public void ShieldOwnerAttacked()

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.SpawnArtifact(System.String[])



        :type parameters: System.String<System.String>[]

        :rtype: Clay.Game.Mod.Entities.Artifact

        .. code-block:: csharp

            public static Artifact SpawnArtifact(string[] parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.SpawnArtifactLua(System.String)



        :type parameters: System.String

        :rtype: Clay.Game.Mod.Entities.Artifact

        .. code-block:: csharp

            public static Artifact SpawnArtifactLua(string parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.Trashed()




        .. code-block:: csharp

            public override void Trashed()

    .. dn:method:: Clay.Game.Mod.Entities.Artifact.Update(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void Update(float time)



